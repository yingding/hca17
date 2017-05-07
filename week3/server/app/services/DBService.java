package services;

import Models.Mood;
import org.jongo.MongoCursor;
import play.api.Play;
import uk.co.panaxiom.playjongo.PlayJongo;

/**
 * @Author Yingding Wang on 07.05.17.
 */
public class DBService {
    // Inject PlayJongo Class
    private static PlayJongo jongo = Play.current().injector().instanceOf(PlayJongo.class);
    private static String MOODS = "moods"; // collection name
    // save a single mood entry
    public static boolean saveMood(Mood mood) {
        return jongo.getCollection(MOODS).save(mood).wasAcknowledged();
    }
    // fetch all moods
    public static MongoCursor<Mood> findAllMoods() {
        return jongo.getCollection(MOODS).find().as(Mood.class);
    }
}
