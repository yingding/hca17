package tasks;

import play.Logger;
import services.DBService;

/**
 * Created by wang on 5/9/17.
 */
public class MoodTasks {
    private static final String TAG = MoodTasks.class.getSimpleName();
    public void countAll() {
        Logger.info("[{}] current total moods is: {}", TAG, DBService.countAllMoods());
    }
}
