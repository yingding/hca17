package Models;

import com.fasterxml.jackson.annotation.JsonProperty;

import java.sql.Time;

/**
 * @author Yingding Wang on 07.05.17.
 */
public class MoodEntry {
    @JsonProperty("_id")
    private Timestamp timestamp;
    //private Timestamp timestamp; // my serializable timestamp object
    private String mood;

    // default constructor needed by Json mapper
    public MoodEntry() {
    }

    public MoodEntry(long timestamp, String mood) {
        this.timestamp = new Timestamp(timestamp);
        this.mood = mood;
    }

    public String toString() {
        return "timestamp:" + timestamp + ", mood:" + mood;
    }

    public Timestamp getTimestamp() {
        return timestamp;
    }

    public void setTimestamp(long timestamp) { this.timestamp = new Timestamp(timestamp); }

    public String getMood() {
        return mood;
    }

    public void setMood(String mood) {
        this.mood = mood;
    }
}
