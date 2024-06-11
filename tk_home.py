import firebase_admin
from firebase_admin import credentials, db

# Initialize the Firebase Admin SDK
cred = credentials.Certificate('carpaldesktopdata-firebase-adminsdk-612ot-6f97dad0fe.json')
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://carpaldesktopdata-default-rtdb.firebaseio.com/'
})

# Reference to the database
ref = db.reference('/')

# Data to be saved
data = {
    'users': {
        'user_1': {
            'first_name': 'Yashwant',
            'last_name': 'Pathak',
            'age': 30
        },

    }
}

# Save data to Firebase Realtime Database
ref.set(data)

print("Data saved successfully!")