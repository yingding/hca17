package modules;

import com.google.inject.AbstractModule;
import play.Environment;
import play.Configuration;
import play.Logger;
import services.AppConfigService;
import services.DaemonService;

/**
 * @Author: Yingding Wang on 07.05.17.
 */
public class AppModule extends AbstractModule {

    private final Environment environment;
    private final Configuration configuration;

    public AppModule(Environment environment, Configuration configuration) {
        this.environment = environment;
        this.configuration = configuration;
    }

    @Override
    public void configure() {
        final Configuration sysVars = configuration.getConfig("myApp");
        //Configuration config = configuration.getConfig("app");
        Logger.info("Starting Demo Server");

        // Ask Guice to create an instance of AppConfigService when the application starts
        bind(AppConfigService.class).asEagerSingleton();
        // Ask Guice to create an instance of AppMongoClientFactory when the application starts
        bind(DaemonService.class).asEagerSingleton();

    }
}
