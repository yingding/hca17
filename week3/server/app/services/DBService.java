package services;

import Models.MoodEntry;
import Models.MoodObject;
import com.mongodb.DBObject;
import com.mongodb.LazyDBObject;
import org.jongo.MongoCursor;
import org.jongo.ResultHandler;
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
    public static boolean saveMood(MoodEntry mood) {
        return jongo.getCollection(MOODS).save(mood).wasAcknowledged();
    }
    // fetch all moods
    public static MongoCursor<MoodObject> findAllMoods() {
        // sort _id (timestamp) descending with -1
        return jongo.getCollection(MOODS).find().sort("{_id: -1}").map(moodResultHandler());
    }

    public static long countAllMoods() {
        return jongo.getCollection(MOODS).count("");
    }

    private static ResultHandler<MoodObject> moodResultHandler() {
        return new ResultHandler<MoodObject>() {
            @Override
            public MoodObject map(DBObject result) {
                Object id = result.get("_id");
                long timestamp;
                try {
                    timestamp = (long) ((LazyDBObject) id).get("timestamp");
                } catch (ClassCastException e) {
                    timestamp = (long) id;
                }
                String mood = (String) result.get("mood");
                return new MoodObject(timestamp, mood);
            }
        };
    }
}
