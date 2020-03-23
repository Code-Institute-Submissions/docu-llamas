# Stitching Life.

test This website is a dedicated to people that enjoy crocheting, knitting and sewing as hobby or way of life.  The purpose of the app is to aggregate different patterns and articles related to the theme. The user is able to create, read, update and delete (CRUD) entries.

## UX
My goal is to create a user-friendly interactive Data-Centric development project. The color scheme was taken from the predominant colours of the picture in the Home section.

### Color Scheme:
I used:
* balboa coolersList

## User Stories
"As a user, I want:"
* To visit a website where I can get patterns, ideas and articles regarding crochet, knitting and sewing.
* To view the website in different devices (mobile, tablet and laptop).
* To add new patterns and articles.
* To edit existent patterns and articles.
* To delete existent patterns and articles.

## Deployment
### Local Deployment
To run the project locally, you need an Integrated development environment and have installed:
* PIP
* Git
* Python
* Mongo DB

After installing these you need to:
1. Download this repository clicking in ‘Clone or Dowload’ on top of this page, then click on ‘Download ZIP’ and extract the files in the folder you will be working on.
2. Open the folder where you download the repository in your code editor
3. Create a `.env` file containing your MongoDB credentials		`MONGO_URI='mongodb+srv://<username>:<password>@<cluster_name>-qtxun.mongodb.net/<database_name>?retryWrites=true&w=majority'`
4. Install the required modules using this command:
`pip -r requirements.txt`
5. Create a new MongoDB database and name it ‘stitching’, then create these three collections:
* patterns	
* pattern_category			
* categories
5. Set host and port to the following:	
```
if __name__ == '__main__': 		
    app.run(
        port=8080,
        debug=True	
    )
```
The project will run at http://127.0.0.1:5000

