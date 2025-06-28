from django.shortcuts import render
from .forms import NumberForm
from pymongo import MongoClient

def process_numbers(request):
    result = {}
    if request.method == 'POST':
        form = NumberForm(request.POST)
        if form.is_valid():
            nums = [form.cleaned_data['a'], form.cleaned_data['b'], form.cleaned_data['c'],
                    form.cleaned_data['d'], form.cleaned_data['e']]

            average = sum(nums) / 5
            is_above_50 = average > 50
            positive_count = len([x for x in nums if x > 0])
            even_odd = ["Even" if x & 1 == 0 else "Odd" for x in nums]
            over_10_sorted = sorted([x for x in nums if x > 10])

            result = {
                'original': nums,
                'average': average,
                'is_above_50': is_above_50,
                'positive_count': positive_count,
                'even_odd': even_odd,
                'over_10_sorted': over_10_sorted
            }

            try:
                client = MongoClient("mongodb://172.31.82.24:27017/")
                db = client.assignment6
                db.results.insert_one({'input': nums, 'result': result})
                client.close()
            except:
                pass

    else:
        form = NumberForm()
    return render(request, 'bitwise/result.html', {'form': form, 'result': result})
