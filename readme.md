This project leverages Machine Learning to predict the churn/default possibility for teleco customers basis the given dataset in csv format. 
The model is then deployed using FastAPI which can be run locally to get the desired prediction. Furthermore, the model can be run on a docker as well.

Steps to run the .ipynb file
1) Download the project and save to the desired location.
2) Open the finantier-test.ipynb file 
3) Run all the cells
(The above steps will ensure all the packages and libraries are downloaded, and uses Logistic Regression model to classify whether the customer will default or not)

Steps to run using locally using FastAPI (Using Python)
1) Download the project and save to the desired location.
2) Open Command Prompt on Windows or Terminal on MAC OS at a location where this project directory is saved.
3) Run python main.py
4) Navigate to localhost:8000/docs to check if API endpoint is working
5) Click on execute with the following input parameters to get the desired output.

API Input parameters:
    gender: float

    SeniorCitizen: float

    Partner: float

    Dependents: float

    tenure: float

    PhoneService: float

    MultipleLines: float

    OnlineSecurity: float
    
    OnlineBackup: float

    DeviceProtection: float

    TechSupport  : float

    StreamingTV : float

    StreamingMovies: float


    PaperlessBilling: float


    MonthlyCharges: float

    TotalCharges: float

    InternetService_DSL : int
    
    InternetService_Fiberoptic: int
    
    InternetService_No: int
    
    c_Month: int
    
    c_Oneyear: int
    
    c_Twoyear: int
    
    PaymentMethod_Bank: int
    
    PaymentMethod_Credit: int
    
    PaymentMethod_Electronic: int
    
    PaymentMethod_Mailed: int


Steps to run on Docker
1) Download the project and save to the desired location.
2) Open Command Prompt on Windows or Terminal on MAC OS at a location where this project directory is saved.
3) Build the docker image using command: docker build -t fast_img .
4) Once the Dockerfile is ran successfully and image is built, run the docker container using command: 
docker run -d --name mycontainer -p 8000:80 fast_img
4) Navigate to localhost:8000/docs to check if API endpoint is working
5) Click on execute with the above input parameters to get the desired output.