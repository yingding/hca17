package daemons;

import akka.actor.ActorSystem;
import akka.actor.Cancellable;
import com.typesafe.config.Config;
import play.Logger;
import play.inject.ApplicationLifecycle;
import scala.concurrent.duration.FiniteDuration;

import java.util.Date;
import java.util.concurrent.CompletableFuture;
import java.util.concurrent.TimeUnit;

/**
 * @Author: Yingding Wang on 07.05.17
 */

public abstract class TemplateDaemon {
    protected Cancellable handle;
    protected String tag;
    private final static String TAG_key  = TemplateDaemon.class.getCanonicalName();
    protected long delayInterval;
    protected long executionIntervalInSec;
    private final static String delayInterval_key = "templateDaemon.delay";
    private final static String executionInterval_key = "templateDaemon.executionInterval";
    protected ActorSystem actorSystem;

/*    protected TemplateDaemon() {
        throw new UnsupportedOperationException("Default Constructor not allowed in " + this.getClass().getCanonicalName());
    }
    */
    public TemplateDaemon() {

    }

    //</editor-fold>
    public TemplateDaemon(ActorSystem actor, ApplicationLifecycle lifecycle, final Config appConf) {
        //TODOs, codes to extract your config
        init(actor, lifecycle, appConf, TAG_key, delayInterval_key, executionInterval_key);
        setup(delayInterval,executionIntervalInSec, templateDaemon);

    }

    protected void init(ActorSystem actor, ApplicationLifecycle lifecycle, final Config appConf, String TAG_key, String delayInterval_key, String executionInterval_key) {
        actorSystem = actor;
        tag = TAG_key;
        try {
            delayInterval = appConf.getLong(delayInterval_key);
            executionIntervalInSec = appConf.getLong(executionInterval_key);
        } catch (Exception e) {
            // set the defaults
            delayInterval = 60;
            executionIntervalInSec = 600; // every ten minutes
            Logger.error("Config Data of {} can not be loaded /n {}", tag, e.getMessage());
        }

        lifecycle.addStopHook(() -> {
            shutdown();
            return CompletableFuture.completedFuture(null);
        });
    }

    public void setup(long delayInterval, long executionIntervalInSec, Runnable daemon) {
        final FiniteDuration delay = FiniteDuration.create(delayInterval, TimeUnit.SECONDS);
        final FiniteDuration freq = FiniteDuration.create(executionIntervalInSec, TimeUnit.SECONDS);
        Logger.info("{} is executed every {} seconds", tag, executionIntervalInSec);

        handle = actorSystem.scheduler().schedule(delay, freq, daemon, actorSystem.dispatcher());
    }

    final Runnable templateDaemon = () -> {
        try {
            final long now = new Date().getTime();
            Logger.info("{} executed at {}", tag, now);
        } catch (Exception e) {
            Logger.error("Error in {} {}", tag, e.getMessage());
        }
    };

    public void shutdown() {
        if (handle != null && !handle.isCancelled()) {
            handle.cancel();
            handle = null;
            Logger.info("{} is shut down.", tag);
        }
    }
}
