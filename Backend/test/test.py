def test_register():
    app = Flask(__name__)
    app.testing = True
    client = app.test_client()

    # Send a PUT request to the "/register" endpoint with JSON data
    response = client.put('/register', json={'email': 'test@example.com', 'fullName': 'Test User'})

    # Check the response status code
    assert response.status_code == 200

    assert b'Content updated' in response.data



def test_login():
    app = Flask(__name__)
    app.testing = True
    client = app.test_client()

    response = client.put('/login', json={'email': 'test@example.com'})

    assert response.status_code == 200

    assert b'full_name' in response.data



def test_track():
    app = Flask(__name__)
    app.testing = True
    client = app.test_client()

    # Send a PUT request to the "/track" endpoint with JSON data
    response = client.put('/track', json={'link': 'https://www.amazon.com/dp/B07VJYZF24', 'toggleValue': 0, 'email': 'test@example.com'})

    # Check the response status code
    assert response.status_code == 200

    # Check the response data
    assert b'email' in response.data
    assert b'productName' in response.data
    assert b'asinServer' in response.data
    assert b'imageUrl' in response.data
    assert b'currentPrice' in response.data
    assert b'productLink' in response.data


def test_fetchCards():
    app = Flask(__name__)
    app.testing = True
    client = app.test_client()

    # Send a PUT request to the "/fetchCards" endpoint with JSON data
    response = client.put('/fetchCards', json={'email': 'test@example.com'})

    # Check the response status code
    assert response.status_code == 200

    assert b'ASIN' in response.data
    assert b'amazon_link' in response.data
    assert b'product_name' in response.data
    assert b'image_link' in response.data
    assert b'curr_price' in response.data

