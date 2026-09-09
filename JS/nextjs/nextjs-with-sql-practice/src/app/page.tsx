import Image from "next/image";
import styles from "./page.module.css";

//components
import { LoginForm } from "@/components/loginForm";

export default function Home() {
  return (
    <div>
      <h1>page is up</h1>
      <LoginForm />
    </div>
  );
}
