import { Injectable } from '@angular/core';
import {HttpClient, HttpClientModule, HttpHeaders} from '@angular/common/http';
import {FormsModule, ReactiveFormsModule} from '@angular/forms';
import {Observable} from 'rxjs' 

@Injectable({
  providedIn: 'root'
})
export class SharedService {

  readonly APIurl = "http://127.0.0.1:5000";
  constructor(private http:HttpClient) { }

  ConvertMarkdown(val:any){
    const headers: HttpHeaders = new HttpHeaders({'Accept': 'text/html'});
    return this.http.post(this.APIurl+'/convert', val, { headers: headers, responseType: 'text' });
  }
}
