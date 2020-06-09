# desktop notifier using win10toast.
import win10toast
toaster = win10toast.ToastNotifier()
toaster.show_toast('Python', "hey there !!!", duration=5) # duration is set for 5 seconds.
toaster.show_toast('Python', "how r u !!!", duration=5)
toaster.show_toast('Python', "U are having work to do !!!", duration=5)
toaster.show_toast('Python', "meeting at 5 pm", duration=5)
toaster.show_toast('Python', "all the best. :)", duration=5)
