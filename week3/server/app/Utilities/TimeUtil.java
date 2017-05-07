package Utilities;

import java.text.Format;
import java.text.SimpleDateFormat;
import java.util.Date;

/**
 * Created by yingding on 07.05.17.
 */
public final class TimeUtil {
    private static final Format formatter = new SimpleDateFormat("yyyy-MM-dd HH:mm:ss");
    public static String getDateStr(Date date) {
        return formatter.format(date);
    }
}
