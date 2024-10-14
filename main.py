from fastapi import FastAPI, Query
from fastapi import Request
from typing import List
from pydantic import BaseModel
#import uvicorn

class JobResult(BaseModel):
    jobid: str
    stdout: str
    stderr: str
    status: int

app = FastAPI()

def _job(next: str):
    print(next)
    return {
        "job": [
            {
                "jobid": "123-1",
                "command": "fping -g 8.8.8.5 8.8.8.10 -r 2 -a -q",
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

@app.get("/job")
async def job(next: str | None = None):
    return _job(next=next)

@app.post("/job")
async def postjob(jobRet: List[JobResult], next: str | None = None): #jobRet: JobResult
    for i, job in enumerate(jobRet):
        print(job.jobid, job.stdout, job.stderr, job.status)
    #print(request)
    #jobResult = jobRet.dict()
    #jobResult = await request.json()
    #print(jobResult)
    return _job(next=next)

#if __name__ == "__main__":
#    uvicorn.run(app, host="0.0.0.0", port=8080)
