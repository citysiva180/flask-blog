from website import create_app


# Creating an instance with custom app creation package
if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
