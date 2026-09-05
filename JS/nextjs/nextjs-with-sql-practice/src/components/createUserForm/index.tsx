export const CreateUserForm = () => {
    return (
        <div>
            <h1>Create User</h1>
            <form>
                <input type="text" placeholder="username" name="username" />
                <input type="password" placeholder="password" name="password" />
                <button type="submit">Create</button>
            </form>
        </div>
    );
}