from django.shortcuts import render
import razorpay
from django.views.decorators.csrf import csrf_exempt


def home(request):
    if request.method == "POST":
        name = request.POST.get('name')
        amount = 50000

        client = razorpay.Client(
            auth=("rzp_test_VK37VPpleXfket", "'OsDSyNEhPzRe0wh7TWlkCZAg"))

        payment = client.order.create({'amount': amount, 'currency': 'INR',
                                       'payment_capture': '1'})
    return render(request, 'index.html')

@csrf_exempt
def success(request):
    return render(request, "success.html")