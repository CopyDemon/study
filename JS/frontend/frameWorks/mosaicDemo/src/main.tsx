import React from "react";
import ReactDOM from 'react-dom/client'
import App from "./App";

import { Button } from "@blueprintjs/core";
import { Download, GitRepo } from "@blueprintjs/icons";

ReactDOM.createRoot(document.getElementById('root')!).render(
  <React.StrictMode>
    <App />
    <div className="my-app"></div>
    <Button text="Download" icon={<GitRepo size={16} />} />
  </React.StrictMode>,
)
