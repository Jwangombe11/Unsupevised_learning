Getting Started with Streamlit for Data Science
Welcome to Getting Started with Streamlit for Data Science! I'm the author, Tyler Richards, and I'm currently a Facebook employee who loved a Python library so much that I wrote a book about it.
If you're coming here from the book, go ahead and take a peak inside each one of the sub-folders in this main repo. You can feel free to clone this repository, and if anything doesn't work you can always open an issue or pull request or just find me on Twitter and DM me until I figure it out.
If you're coming here from another place on the internet, feel free to use these respositories and examples however you would like! They are more useful in context, and so I would obviously recommend giving the book a shot. If you're a young data scientist who can't afford the book, please reach out to me and I'd be happy to provide a copy no questions asked.
The first chapter starts in the folder 'clt_app', head over there with the book in hand and enjoy!

Book Edits
Streamlit is an ever-changing library, and by the time this book was written it was already slightly behind compared to newer versions of the library. If you notice error messages, please message me about them so I can get them all fixed or note them below!

st.beta_columns is out of beta! As of now, st.beta_columns is now called simply st.columns! Excited to see this one out of beta, and depending on your Streamlit version you will get an error if you use st.beta_columns
There is an open bug caused when you redirect the output of 'streamlit config show' to the config.toml file for your project, I would instead copy and paste this manually! See this post for more info
