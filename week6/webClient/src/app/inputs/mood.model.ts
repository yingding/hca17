export class MoodModel {
    timestamp: number; // https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Number/MAX_SAFE_INTEGER
    mood: string
    constructor(timestamp : number, moodStr: string ) {
        this.timestamp = timestamp;
        this.mood = moodStr;
    }
}