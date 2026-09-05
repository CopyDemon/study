import { Injectable } from '@angular/core';
import { Observable, Observer } from 'rxjs';
@Injectable({
  providedIn: 'root'
})
export class UserFormService {
  public userFormData: any;
  
  constructor() {}

  alertUserFormData() {
    const data = this.userFormData.then((data:any) => {
      alert(JSON.stringify(data));
    });
  }

  getRemoteUserFormData(url: string){
    return new Observable<any>(observer=>{
      const data = fetch(url)
            .then((response)=>response.json())
            .catch((error)=>{console.log(error)});
      observer.next(data);
      observer.complete(/*TODO: learn what can do inside complete */);
    });
  }
}
