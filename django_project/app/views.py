from rest_framework.views import APIView
from rest_framework.response import Response
from .tasks import add

class AddView(APIView):
    # def get(self, request, *args, **kwargs):
    #     task = add.delay(5, 7)
    #     return Response({"task_id": task.id, "status": "Task Sent"})

    def get(self, request, *args, **kwargs):
        print('---------------------- get start -------------------------')
        result = add.delay(4, 6)  # Asynchronous task
        
        print('ADD TASK IS DONE...')
        print(result.id)  # Print the unique task ID
        print(result.status)  # Check the task status (e.g., 'PENDING', 'SUCCESS')
        print('---------------------- get end returning task id -------------------------')
        return Response({"task_id": result.id, "status": "Task Sent"})
