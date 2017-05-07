package daemons;

import Utilities.TimeUtil;
import akka.actor.ActorSystem;
import com.typesafe.config.Config;
import play.Logger;
import play.inject.ApplicationLifecycle;

import java.text.Format;
import java.text.SimpleDateFormat;
import java.util.Date;


public class ExampleDaemon extends TemplateDaemon {
    private final static String TAG_key = ExampleDaemon.class.getCanonicalName();
    private static final String delayInterval_key = "exampleDaemon.delay";
    private static final String executionInterval_key = "exampleDaemon.executionInterval";

    public ExampleDaemon() {
        super();
    }

    public ExampleDaemon(ActorSystem actor, ApplicationLifecycle lifecycle, final Config appConf) {
        super.init(actor, lifecycle, appConf, TAG_key, delayInterval_key, executionInterval_key);
        setup(delayInterval, executionIntervalInSec, exampleDaemon);
    }

    final Runnable exampleDaemon = () -> {
        try {
            /* getTime() return a utc timestamp
             * final long now = new Date().getTime();
             */
            final String now = TimeUtil.getDateStr(new Date());
            Logger.info("{} executed at {}", tag, now);
        } catch (Exception e) {
            Logger.error("Error in {} {}", tag, e.getMessage());
        }
    };
}

