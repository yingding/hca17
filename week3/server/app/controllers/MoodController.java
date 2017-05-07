package controllers;

import Models.Mood;
import Utilities.Authentication;
import com.fasterxml.jackson.databind.JsonNode;
import com.google.inject.Inject;
import com.typesafe.config.Config;
import play.Logger;
import play.mvc.BodyParser;
import play.mvc.Controller;
import play.mvc.Result;
import services.AppConfigService;
import services.DBService;


/**
 * Created by yingding on 07.05.17.
 */
public class MoodController extends Controller {

    private final Config appConf;

    @Inject
    public MoodController(AppConfigService appConfService) { this.appConf = appConfService.getConfig();}

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
                Mood mood = new Mood(
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
            return ok("moods saved successfully");
        } else {
            return badRequest("moods has inapproperate structure, can not be all saved");
        }
    }
}
