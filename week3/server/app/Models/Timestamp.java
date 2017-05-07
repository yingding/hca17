package Models;

import java.io.Serializable;

public class Timestamp implements Serializable {

    private long timestamp;

    public Timestamp() {}

    public Timestamp(long timestamp) {
        this.timestamp = timestamp;
    }

    public long getTime() {
        return timestamp;
    }

    @Override
    public String toString() {
        return "Timestamp:" + this.timestamp;
    }
}
