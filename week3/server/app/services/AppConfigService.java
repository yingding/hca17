package services;

/**
 * Created by yingdingwang on 5/5/17.
 */

import com.typesafe.config.Config;
import com.typesafe.config.ConfigFactory;
import play.Configuration;
import play.Logger;

import javax.inject.Inject;
import javax.inject.Singleton;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.IOException;

@Singleton
public final class AppConfigService {
    private final static String STR_APP_HOME = "home"; // Variable defined in application.conf
    private final static String STR_APP_CONF = "config";
    private final static String STR_APP_PREFIX = "myApp";
    private final static String STR_CONF_PREFIX = "app";
    private static Configuration sysConf;
    private static Config APP_CONFIG;

    @Inject
    public AppConfigService(Configuration configuration) throws IOException {
        sysConf = configuration.getConfig(STR_APP_PREFIX);
        try {

            File appConfigFile = new File(sysConf.getString(STR_APP_HOME) + File.separator + sysConf.getString(STR_APP_CONF)).getCanonicalFile();
            if (!appConfigFile.exists())
            {
                throw new FileNotFoundException(appConfigFile.getAbsolutePath());
            }
            Logger.info ("Loading configuration file: {}",  appConfigFile.getAbsoluteFile());
            APP_CONFIG = ConfigFactory.parseFile(appConfigFile).getConfig(STR_CONF_PREFIX);
        } catch (FileNotFoundException e) {
            this.APP_CONFIG = null;
            Logger.error("Error in opening configuration file: {}", e.getMessage());
            // e.printStackTrace();
        }
    }

    public Config getConfig() {
        return this.APP_CONFIG;
    }
}
