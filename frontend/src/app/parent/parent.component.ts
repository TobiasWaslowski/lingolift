import {Component} from '@angular/core';

@Component({
    selector: 'app-parent',
    templateUrl: './parent.component.html',
    styleUrls: ['./parent.component.css']
})
export class ParentComponent {
    sentence: string = '';
    language: string = 'english';

    setSentence(sentence: string) {
        this.sentence = sentence;
    }
}