package controllers;

import Models.MoodEntry;
import Models.MoodObject;
import Utilities.Authentication;
import Utilities.TimeUtil;
import akka.actor.ActorSystem;
import com.fasterxml.jackson.databind.JsonNode;
import com.fasterxml.jackson.databind.node.ObjectNode;
import com.google.inject.Inject;
import com.typesafe.config.Config;
import daemons.ExampleDaemon;
import play.Logger;
import play.api.Play;
import play.libs.Json;
import play.mvc.BodyParser;
import play.mvc.Controller;
import play.mvc.Result;
import scala.concurrent.duration.FiniteDuration;
import services.AppConfigService;
import services.DBService;
import tasks.MoodTasks;

import java.util.Date;
import java.util.Iterator;
import java.util.concurrent.TimeUnit;


/**
 * Created by yingding on 07.05.17.
 */
public class MoodController extends Controller {

    private final Config appConf;
    private ActorSystem actorSystem;

    @Inject
    public MoodController(AppConfigService appConfService, ActorSystem actorSystem) {
        this.appConf = appConfService.getConfig();
        this.actorSystem = actorSystem;
    }

    @BodyParser.Of(BodyParser.Json.class)
    public Result saveMoodInput() {
        boolean succeed = true;
        boolean canBeSaved;
        // parse the body
        JsonNode json = request().body().asJson();
        if (json == null) {
            return badRequest("Expecting Json data");
        }
        String requestTcpSeed = json.findPath("seed").asText();
        if (Authentication.isAuthorizedSeed(appConf, requestTcpSeed)) {
            JsonNode moods = json.findPath("moods");
            for (JsonNode moodNode : moods) {
                MoodEntry mood = new MoodEntry(
                        moodNode.findPath("timestamp").asLong(),
                        moodNode.findPath("mood").asText()
                );
                canBeSaved = DBService.saveMood(mood);
                if (canBeSaved) {
                    Logger.info("Inserted " + mood.toString());
                } else {
                    Logger.info("Failed to insert " + mood.toString());
                    succeed = false;
                    break; // break out the for loop, must not always be breakded out.
                }
            }
        } else {
            return unauthorized("Unauthorized seed");
        }
        if (succeed) {
            // run a async task
            runAsyncTask();
            return ok("moods saved successfully");
        } else {
            return badRequest("moods has inapproperate structure, can not be all saved");
        }
    }

    /**
     * http://doc.akka.io/docs/akka/current/java/scheduler.html
     * @return
     */
    public Result getAllMoods() {
        Logger.info("Get all Moods on " + TimeUtil.getDateStr(new Date()));
        boolean succeed = true;
        // parse the body
        JsonNode json = request().body().asJson();
        if (json == null) {
            return badRequest("Expecting Json data");
        }
        String requestTcpSeed = json.findPath("seed").asText();
        if (Authentication.isAuthorizedSeed(appConf, requestTcpSeed)) {
            // fetch data from db
            Iterator<MoodObject> moods = DBService.findAllMoods();
            ObjectNode result = Json.newObject();
            result.set("moods", Json.toJson(moods));
            return ok(result);
        } else {
            return unauthorized("Unauthorized seed");
        }
    }

    private void runAsyncTask() {
        // The task shall be run in 1 seconds after the time this task is scheduled
        actorSystem.scheduler().scheduleOnce(FiniteDuration.create(1, TimeUnit.SECONDS), () -> {
            try {
                // in scheduled task, get a instance of task from injector
                MoodTasks moodTasks = Play.current().injector().instanceOf(MoodTasks.class);
                // execute count task
                moodTasks.countAll();
            } catch (Exception e) {
                Logger.error("Error in {}: {}", "MoodTask", e.getMessage());
            }
        }, actorSystem.dispatcher());
    }
}
