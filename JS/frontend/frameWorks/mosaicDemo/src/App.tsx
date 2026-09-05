import './App.css'
import MosaicApp from "./MosaicApp";
import { useEffect } from 'react';

export default function App(){
  useEffect(()=>{
    const mw = document.querySelector(".mosaic-blueprint-theme") as HTMLElement
    mw.style.height = "100vh"
    mw.style.width = "100vh"
    console.log(mw)
  },[])
  return(
    <div>
      <h1>app</h1>
      <MosaicApp />
    </div>
  )
}