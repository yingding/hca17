package services;

import akka.actor.ActorSystem;
import com.google.inject.Inject;
import com.google.inject.Singleton;
import daemons.ExampleDaemon;
import daemons.TemplateDaemon;
import play.inject.ApplicationLifecycle;

import java.util.LinkedList;
import java.util.List;
import java.util.concurrent.CompletableFuture;

/**
 * Created by wang on 05.05.17
 */
@Singleton
public class DaemonService {
    protected static List<TemplateDaemon> daemonQueue;
    @Inject
    public DaemonService(ActorSystem actorSystem, ApplicationLifecycle lifecycle, AppConfigService appConf) {
        daemonQueue = new LinkedList<>();
        // Starting and Queueing all Daemon
        daemonQueue.add(new ExampleDaemon(actorSystem, lifecycle, appConf.getConfig()));

        // Todo: Extend Queue for further daemon

        lifecycle.addStopHook(() -> {
            shutdown();
            return CompletableFuture.completedFuture(null);
        });
    }

    private void shutdown() {
        // daemon shutdown will be down be daemons
        daemonQueue.clear();
        daemonQueue = null;
    }
}
