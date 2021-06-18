import { Component, NgZone, OnInit,Input, ViewChild } from '@angular/core';
import { SharedService } from '../shared.service';
import { FormBuilder, Validators, FormGroup, FormControl } from '@angular/forms';


@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css']
})
export class HomeComponent{

  submitted = false
  constructor(private service:SharedService) { }
  @ViewChild('TextForm') form: any;
  showresults : any;
  OnSubmit(data: any){
    // this.form.reset();
    this.service.ConvertMarkdown(data).subscribe(res=>{
      this.showresults = res;
      // alert(res.toString());
    });
  }


}
