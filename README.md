# shopify-image-repo

Shopify Instagram-like clone

A simple application that allows the user to create an account, upload an image, and if the user is an admin(staff) or original author, the ability to delete the image. I have left the ability to post comment out in the model, but did not implement it purposely to show that it can be a feature added. This can be seen in the models and also supports ability to edit comments made to posts.

I apologize for not creating multiple apps and properly splitting up the models, forms, and views in advance, but I felt this little application was still small enough to be done in this simple way.

Instructions:

Please clone the project from the GitHub link.

In the terminal do change the directory into the cloned repository.

Now type 'poetry install' into your terminal.

Now enter the venv by typing in 'poetry shell'.

Now run the migrations by typing "python manage.py makemigrations" into your terminal.

After that migrate everything by typing in "python manage.py migrate" into your terminal.

_Optional_ you can create a superuser with the "python manage.py createsuperuser" command.

Once that has loaded feel free to run the application by typing in "python manage.py runserver" into your terminal and access it on your web browser with the provided hosted link.

Application Instructions:

Users will be unable to view posts made by members without first logging into the application.

Upon loading you should immediately be greeted by a login screen and near the button should be a Sign Up link. Go ahead and click on Signup.

You will now be redirected to a sign up view that looks very similar to the login page. Go ahead and sign up using any username and password that you like and you will automatically be logged in as well.

Feel free to click on the Upload link and be directed to a new screen that allows you to upload an image from your computer. You can also post any comment you have about it under the body field. _comments feature left out intentionally for now_.

Upon uploading an image you will be redirected to the home page where you can see your image loaded. Feel free to click on the comment and be directed to that post directly.

In this view you may notice a "Delete" button at the bottom, but do know that this option only appears for admin users and authors of the image.

Thank you using Shopigram!

Author: Billy Yip
