from fastapi import FastAPI
from fastapi import Request
from pydantic import BaseModel
#import uvicorn

class JobResult(BaseModel):
    jobid: str
    stdout: str
    stderr: str

app = FastAPI()

@app.get("/job")
async def job():
    return {
        "job": [
            {
                "jobid": "123-1",
                "command": "fping --help",
            },
            {
                "jobid": "123-2",
                "command": "fping -g 1.1.1.0 1.1.1.3 -r 2 -a -q",
            },
            {
                "jobid": "123-3",
                "command": "fping -g 110.242.68.1 110.242.68.10 -r 2 -a -q",
            },
        ],
        "next": "sfkR1xjer",
        "interval": 10,
        "status": 200
    }

@app.post("/job")
async def postjob(request: Request): #jobRet: JobResult
    print(request)
    #jobResult = jobRet.dict()
    jobResult = await request.json()
    print(jobResult)
    return job()

#if __name__ == "__main__":
#    uvicorn.run(app, host="0.0.0.0", port=8080)
