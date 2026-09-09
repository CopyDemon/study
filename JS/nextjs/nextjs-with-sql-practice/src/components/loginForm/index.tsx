'use client' //define client side code
import { fetchData } from "@/utility/fetch";
/**
 * @description Login form component
 * @returns JSX.Element <LoginForm> : login form main component
 */
export const LoginForm = () => {
    const handleSubmit = async (e: React.FormEvent<HTMLFormElement>) => {
        try {
            e.preventDefault();
            const form = e.target as HTMLFormElement;

            const response = await fetchData("/api/login", "GET", {
                username: form.username.value,
                password: form.password.value
            })

            // window.localStorage.setItem("webToken", response.webToken);
        } catch (error) {
            console.log(`Fail to login: ${error}`);
        }
    }
    return (
        <div>
            <form onSubmit={handleSubmit}>
                <input type="text" placeholder="username" name="username" />
                <input type="password" placeholder="password" name="password" />
                <button type="submit">Login</button>
            </form>
            <div>
                <a href="/createUser">Create User</a>
                <a href="/forgetPassword">Forget ID or Password</a>
            </div>
        </div>
    );
}
