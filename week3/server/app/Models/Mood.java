package Models;

import com.fasterxml.jackson.annotation.JsonProperty;

/**
 * @author Yingding Wang on 07.05.17.
 */
public class Mood {
    @JsonProperty("_id")
    private Timestamp timestamp; // my serializable timestamp object
    private String mood;

    // default constructor needed by Json mapper
    public Mood() {
    }

    public Mood(long timestamp, String mood) {
        this.timestamp = new Timestamp(timestamp);
        this.mood = mood;
    }

    public String toString() {
        return this.timestamp.toString() + "mood:" + mood;
    }

    public Timestamp getTimestamp() {
        return timestamp;
    }

    public void setTimestamp(long timestamp) {
        this.timestamp = new Timestamp(timestamp);
    }

    public String getMood() {
        return mood;
    }

    public void setMood(String mood) {
        this.mood = mood;
    }
}
