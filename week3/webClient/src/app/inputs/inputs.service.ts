import {Injectable} from '@angular/core';
import {MoodModel} from './mood.model';

@Injectable()
export class MoodsService {
    API_URL = "api/moods/"
   getMoods(): void {

   }
   sendMoods(moods : MoodModel[]): void {

   }
}