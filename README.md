
# Tech Connect

Tech Connect is a social networking platform designed for tech enthusiasts to connect, share experiences, and collaborate on projects. This project is built using Django and Django REST framework.

## Features

- User Authentication (Sign Up, Login)
- User Profiles with Experience and Education details
- Create, Read, Update, and Delete Posts
- Like and Comment on Posts
- Fetch GitHub Repositories for Users

## Installation

1. **Clone the repository:**
   ```sh
   git clone https://github.com/yourusername/Tech-Connect.git
   cd Tech-Connect
   ```

2. **Create and activate a virtual environment:**
   ```sh
   python -m venv .venv
   .\.venv\Scripts\activate  # On Windows
   source .venv/bin/activate  # On macOS/Linux
   ```

3. **Install the required packages:**
   ```sh
   pip install -r requirements.txt
   ```

4. **Apply migrations:**
   ```sh
   python manage.py migrate
   ```

5. **Run the development server:**
   ```sh
   python manage.py runserver
   ```

## API Endpoints

- **User Registration:** `/api/users/`
- **User Login:** `/api/auth/login/`
- **User Profile:** `/api/profile/`
- **Posts:** `/api/posts/`
- **Comments:** `/api/posts/<post_id>/comments/`
- **Like/Unlike Post:** `/api/posts/<post_id>/like/`
- **GitHub Repositories:** `/api/github/<username>/`

## Contributing

We welcome contributions to improve Tech Connect. Please follow these steps to contribute:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes and commit them (`git commit -m 'Add new feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Create a new Pull Request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For any inquiries or feedback, please contact us at [jafaruomeiza2@gmail.com].

#EddieMujafar