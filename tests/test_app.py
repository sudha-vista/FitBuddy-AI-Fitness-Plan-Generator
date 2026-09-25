def payload(user_id="test001"):
    return {"username":"Test User","user_id":user_id,"age":24,"weight":68,"goal":"muscle gain","intensity":"medium"}

def test_home(client):
    r=client.get("/")
    assert r.status_code==200 and "FitBuddy" in r.text

def test_health(client):
    r=client.get("/api/health")
    assert r.status_code==200 and r.json()["status"]=="ok"

def test_create_get_update(client):
    r=client.post("/api/plans",json=payload())
    assert r.status_code==201
    assert "Day 1" in r.json()["workout_plan"]
    assert client.get("/api/users/test001").status_code==200
    r=client.post("/api/plans/test001/feedback",json={"feedback":"Add more cardio and one extra rest day."})
    assert r.status_code==200 and r.json()["updated_plan"]

def test_duplicate(client):
    assert client.post("/api/plans",json=payload()).status_code==201
    assert client.post("/api/plans",json=payload()).status_code==409

def test_form(client):
    r=client.post("/generate-workout",data={"username":"Form User","user_id":"form001","age":"25","weight":"62","goal":"general wellness","intensity":"low"})
    assert r.status_code==200 and "Original 7-Day Workout Plan" in r.text
