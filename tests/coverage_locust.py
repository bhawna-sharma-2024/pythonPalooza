from locust import HttpUser,task,TaskSet,between
import json
class UserBehaviour(TaskSet):
    @task(1)
    def create_user_and_order_book(self):
        response = self.client.post("/Account/v1/User", json={
             "userName": "bhawnash@hotmail.com",
              "password": "bhawna@12893883"
        })
        if response.status_code == 201:
            user_data = response.json()
            user_id = user_data['userID']  # Extract user ID from the response

        #Get books
            books_response = self.client.get("/BookStore/v1/Books").json()
            isbn=books_response["books"][0]["isbn"]

            # Step 2: Order a book with the created user
            order_response = self.client.post("/BookStore/v1/Books", json={
                              "userId": user_id,
                              "collectionOfIsbns": [
                                {
                                  "isbn": isbn
                                }
                              ]
                            })
            if order_response.status_code == 201:
                print("Order placed successfully")
            else:
                print(f"Failed to place order: {order_response.status_code}")

        else:
            print(f"Failed to create user: {response.status_code}")

class WebsiteUser(HttpUser):
    tasks = [UserBehaviour]
    wait_time = between(1, 5)