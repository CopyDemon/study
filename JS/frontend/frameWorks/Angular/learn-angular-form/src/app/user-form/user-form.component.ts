import { Component,inject } from '@angular/core';
import { FormGroup, FormControl } from '@angular/forms';
import { UserFormService } from '../service/user-form.service';


interface UserFormData {
  title: string,
  userId: number | string,
  id: number | string,
}

/**
 * What this code do
 * 1. Create a form group with a text input field.
 * 2. When submit it read remote data by subscribe the observable from service file.
 * 3. With in the subscribe, has an alert just for test and for fun.
 * 
 * conclusion:
 * The service for angular is use to store some reusable data or function and allow other   
 * component to use those data or function.
 * 
 * Other functions want to use service file, just need to inject the service file and use it.
 */

@Component({
  selector: 'app-user-form',
  templateUrl: './user-form.component.html',
  styleUrls: ['./user-form.component.css']
})
export class UserFormComponent {
  private userFormService = inject(UserFormService);
  public userFormData: UserFormData = {
    title: 'Loading...',
    userId: 'loading...',
    id: 'loading...',
  };

  public c = "陈硬🐍";

  private url = 'https://jsonplaceholder.typicode.com/todos/1'
  constructor() {
  }

  // Create a form group with a text input field
  // Angular use formGroup and formControl to create a form
  userForm = new FormGroup({
    firstName: new FormControl(''),
    lastName: new FormControl(''),
    email: new FormControl(''),
    gender: new FormControl(''),
    text: new FormControl(''),
  });

  // When submit it read remote data by subscribe the observable from service file
  userFormSubmit() {
    console.log(this.userForm.value);
    // Get the remote data from service file
    const userDataObservable = this.userFormService.getRemoteUserFormData(this.url);
    // Subscribe the observable and assign the data to userFormData
    userDataObservable.subscribe((data:any)=>{
      data.then((data:any)=>{ 
        this.userFormData = data;
      });
    });
    // Alert the text input field value just for test and for fun 
    alert(`${this.userForm.value.text}爱${this.c}`);
  }
}
