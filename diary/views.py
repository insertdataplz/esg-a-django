from django.contrib import messages
from django.shortcuts import render, redirect
from diary.models import Memory
from diary.forms import MemoryForm

def memory_list(request):
    memory_qs = Memory.objects.all()   #.order_by("-id")
    return render(request, "diary/memory_list.html", {
        'memory_list': memory_qs
    })

def memory_detail(request, pk):
    memory = Memory.objects.get(pk=pk)
    return render(request, "diary/memory_detail.html", {
        'memory': memory
    })

def memory_new(request):
    if request.method == "GET":
        form = MemoryForm()
    else:
        form = MemoryForm(request.POST)
        if form.is_valid():
            memory = form.save()
            messages.success(request, "메모리를 저장했습니다.")
            return redirect(memory)
    
    return render(request, "diary/memory_form.html", {
        'form': form
    })


def memory_edit(request, pk):
    memory = Memory.objects.get(pk=pk)

    if request.method == "GET":
        form = MemoryForm(instance=memory)
    else:
        form = MemoryForm(request.POST, instance=memory)
        if form.is_valid():
            memory = form.save()
            messages.success(request, "메모리를 수정했습니다.")
            return redirect(memory)

    return render(request, "diary/memory_form.html", {
        'form': form
    })

def memory_delete(request, pk):
    memory = Memory.objects.get(pk=pk)

    # delete memory
    if request.method == "POST":
        memory.delete()
        messages.success(request, "메모리를 삭제했습니다.")
        return redirect("/diary/")

    return render(request, "diary/memory_confirm_delete.html", {
        "memory": memory,
    })