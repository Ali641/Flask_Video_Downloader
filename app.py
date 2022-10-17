from flask import Flask, render_template, request, redirect
import youtube_dl
app = Flask(__name__)

@app.route('/')
def home():
	return render_template('index.html')

#@app.route('/about')
#def about():
#	return render_template('blog.html')

@app.route('/terms-conditions')
def terms():
	return render_template('terms_conditions.html')

@app.route('/contact_us')
def contact():
	return render_template('contact.html')

@app.route('/download', methods=["POST", "GET"])
def download():
	url = request.form["url"]
	print("Someone just tried to download", url)
	with youtube_dl.YoutubeDL() as ydl:
		url = ydl.extract_info(url, download=False)
		print(url)
		try:
			download_link = url["entries"][-1]["formats"][-1]["url"]
		except:
			download_link = url["formats"][-1]["url"]
		return redirect(download_link+"&dl=1")
	return redirect(url_for('home'))

if __name__ == '__main__':
	app.run(port=80, debug=True)