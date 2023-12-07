from playwright.sync_api import sync_playwright
import argparse
import getpass
import os
from bs4 import BeautifulSoup


def main():
	os.system('cls')
	with sync_playwright() as p:
		browser = p.firefox.launch(headless=False)

		page = browser.new_page()

		page.goto("https://www.linkedin.com/", timeout=9000)
		page.wait_for_timeout(1000)
		signin_xpath='//label[contains(text(), "Email or phone")]'
		signin_link = page.locator(signin_xpath)
	   
		if signin_link:
			signin_link.click()
			page.wait_for_timeout(1000)
	   
			page.locator('//input[@name="session_key"]').fill(email)
			page.wait_for_timeout(3000)

			page.locator('//input[@name="session_password"]').fill(password)
			page.wait_for_timeout(2000)

			page.keyboard.press("Enter")
			page.wait_for_timeout(2000)

			page.wait_for_timeout(3000)
			compose_xpath='//nav[@class="global-nav__nav"]//li[3]'
			compose_button=page.locator(compose_xpath)
			if compose_button:
				compose_button.click()
				page.wait_for_timeout(1000)
				job
				page.locator('//input[@aria-label="Search by title, skill, or company"][1]').fill(job)
				page.keyboard.press("Enter")
				page.keyboard.press("Backspace")
				page.keyboard.press("Enter")
				page.wait_for_timeout(3000)
				page.locator('//input[@aria-label="City, state, or zip code"][1]').fill(loc)
				page.locator('//button[contains(normalize-space(), "Search")]').click()
				
				page.wait_for_timeout(3000)
				page.locator('//button[contains(normalize-space(),"Easy Apply") and @aria-label="Easy Apply filter."]').click()
				
				previously_counted = 0
				page.hover('//div[contains(@class,"job-card-container relative job-card-list")]')
				while True:

					page.mouse.wheel(0, 40000)

					
					page.wait_for_timeout(4000)
					total=25
					if (page.locator( '//div[contains(@class,"job-card-container relative job-card-list")]').count() >= total):
						listings = page.locator( '//div[contains(@class,"job-card-container relative job-card-list")]').all()[:total]
						listings = [listing.locator("xpath=..") for listing in listings]
						print(f"Total Found: {len(listings)}")
						break
					else: #The loop should not run infinitely
						if (page.locator( '//div[contains(@class,"job-card-container relative job-card-list")]' ).count() == previously_counted ):
							listings = page.locator( '//div[contains(@class,"job-card-container relative job-card-list")]' ).all()
							print(f"Arrived at all available\nTotal Found: {len(listings)}")
							break
						else:
							previously_counted = page.locator( '//div[contains(@class,"job-card-container relative job-card-list")]' ).count()
							print( f"Currently Found: ", page.locator( '//div[contains(@class,"job-card-container relative job-card-list")]' ).count(), )
				
				page.wait_for_timeout(4000)
				for listing in listings:
					listing.click()
					page.wait_for_timeout(5000)
					mobile_phone_xpath='//label[text()="Mobile phone number"]/following-sibling::input[@class=" artdeco-text-input--input"]'
					summary_xpath='//label[text()="Summary"]/following-sibling::textarea'
					cover_letter_xpath='//label[text()="Cover letter"]/following-sibling::textarea'
					next_button_xpath= '//button[@aria-label="Continue to next step"]'
					resume_next_button= '//h3[contains(normalize-space(), "Resume")]/following::button[@aria-label="Continue to next step"]'
					review_button_xpath='//button[@aria-label="Review your application"]'
					submt_button_xpath='//button[@aria-label="Submit application"]'
					done_button_xpath='//button//span[@class="artdeco-button__text" and contains(normalize-space(),"Done")]'
					
				# page.locator('//div[@name="cc"]//input').fill(email_cc)
				# page.wait_for_timeout(1000)
				# page.locator('//div[@name="bcc"]//input').fill(email_bcc)
				# page.locator('//input[@name="subjectbox"]').fill(email_subject)
				# page.locator('//div[@class="Am Al editable LW-avf tS-tW"]').fill(email_text)
				# page.wait_for_timeout(1000)

				# send_xpath='//div[@class="T-I J-J5-Ji aoO v7 T-I-atl L3"]'
				# send_link=page.locator(send_xpath)
				# send_link.click()
				# page.wait_for_timeout(4000)
		browser.close()
		os.system('cls')
		print("Your Mail has been sent successfully\n")
				

if __name__ == "__main__":
	parser = argparse.ArgumentParser()
	parser.add_argument("-e", "--email", type=str)
	parser.add_argument("-p", "--pswd", type=str)
	parser.add_argument("-j","--job", type=str)
	parser.add_argument("-l","--loc", type=str)
	
	# parser.add_argument("-to", "--to", type=str)
	# parser.add_argument("-cc", "--cc", type=str)
	# parser.add_argument("-bcc", "--bcc", type=str)
	# parser.add_argument("-S","--subject", type=str)
	# parser.add_argument("-T", "--text", type=str)
	
	email=recipient=email_cc=email_bcc=email_text=email_subject=""
	args = parser.parse_args()

	if args.email:
		email=args.email
	else:
		email=input("Enter Your Email: ")

	if args.pswd:
		password=args.pswd
	else:
		password = getpass.getpass('Enter Password: ')

	if args.job:
		job = args.job
		job+="."
	else:
		job = input("Enter Job Title: ")
		job+="."
	if args.loc:
		loc = args.loc
		loc+="."
		
   
	  
	# else:
	#     recipient = input("Enter the email of the person you want to mail: ")
	# if args.cc:
	#     email_cc = args.cc
	# if args.bcc:
	#     email_bcc = args.bcc
	# if args.subject:
	#     email_subject = args.subject
	# else:
	#     email_subject = input("Enter Email Subject: ")
	# if args.text:
	#     email_text = args.text
	# else:
	#     email_text = input("Enter the text portion of the mail: ")


	main()