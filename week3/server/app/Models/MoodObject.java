package Models;

/**
 * @author Yingding Wang on 07.05.17.
 */
public class MoodObject {
    private long timestamp;
    //private Timestamp timestamp; // my serializable timestamp object
    private String mood;

    // default constructor needed by Json mapper
    public MoodObject() {
    }

    public MoodObject(long timestamp, String mood) {
        this.timestamp = timestamp;
        this.mood = mood;
    }

    public String toString() {
        return "timestamp:" + timestamp + ", mood:" + mood;
    }

    public long getTimestamp() {
        return timestamp;
    }

    public void setTimestamp(long timestamp) { this.timestamp = timestamp; }

    public String getMood() {
        return mood;
    }

    public void setMood(String mood) {
        this.mood = mood;
    }
}
