import { Component } from '@angular/core';
import { NgIf, NgFor } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { HttpClient, HttpClientModule } from '@angular/common/http';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [NgIf, NgFor, FormsModule, HttpClientModule],
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.sass']
})
export class AppComponent {
  prompt: string = '';
  generatedText: string = '';
  history: { prompt: string, response: string }[] = [];
  loading: boolean = false;

  constructor(private http: HttpClient) {
    this.loadHistory();
  }

  generateText() {
    if (!this.prompt.trim()) return;
    this.loading = true;
    this.http.post<any>('http://127.0.0.1:8000/generate/', { prompt: this.prompt })
      .subscribe(response => {
        this.generatedText = response.generated_text;
        this.history = response.history;
        this.prompt = '';
        this.loading = false;
      });
  }

  loadHistory() {
    this.http.get<any>('http://127.0.0.1:8000/history/')
      .subscribe(response => {
        this.history = response.history;
      });
  }
}
