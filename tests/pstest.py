from parallelsoup import ParallelSoup

urls = [
    'https://www.amazon.in/s?k=ryzen+7&crid=1SP4W73E806YL&sprefix=Ryzen%2Caps%2C550&ref=nb_sb_ss_ts-doa-p_1_5',
    'https://www.amazon.in/s?k=ryzen+7&page=2&crid=1SP4W73E806YL&qid=1616304303&sprefix=Ryzen%2Caps%2C550&ref=sr_pg_2',
    'https://www.amazon.in/s?k=ryzen+7&page=3&crid=1SP4W73E806YL&qid=1616304319&sprefix=Ryzen%2Caps%2C550&ref=sr_pg_2',
    'https://www.amazon.in/s?k=ryzen+7&page=4&crid=1SP4W73E806YL&qid=1616304329&sprefix=Ryzen%2Caps%2C550&ref=sr_pg_3',
    'https://www.amazon.in/s?k=ryzen+7&page=5&crid=1SP4W73E806YL&qid=1616304350&sprefix=Ryzen%2Caps%2C550&ref=sr_pg_4',
    'https://www.amazon.in/s?k=ryzen+7&page=6&crid=1SP4W73E806YL&qid=1616304370&sprefix=Ryzen%2Caps%2C550&ref=sr_pg_5',
    'https://www.amazon.in/s?k=ryzen+7&page=7&crid=1SP4W73E806YL&qid=1616304383&sprefix=Ryzen%2Caps%2C550&ref=sr_pg_6',
    'https://www.amazon.in/Intel-i9-10900X-Desktop-Processor-Unlocked/dp/B07YP69HTM/ref=sr_1_97?crid=1SP4W73E806YL&dchild=1&keywords=ryzen+7&qid=1616304410&sprefix=Ryzen%2Caps%2C550&sr=8-97'
]

ps = ParallelSoup(8, urls)
ps.start()
print(ps.get())
