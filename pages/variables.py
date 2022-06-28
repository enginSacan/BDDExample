class Variables:
    """
        This class is for the variables which are related with the web elements
        based on id, css, xpath or other selectors.
    """
    # Search Page Variables
    search_bar_xpath = "//input[@class='gLFyf gsfi']"
    search_btn_xpath = "//div[@class='FPdoLc lJ9FBc']//input[@class='gNO89b']"
    search_result_url_xpath = "//div[@class='TbwUpd NJjxre']//cite[@class='iUh30 tjvcx']"
    search_result_xpath = "//cite[contains(@class,'iUh30') and contains(@class,'tjvcx')]"
    google_icon_xpath = "//img[@class='lnXdpd']"
    accept_btn_id = "L2AGLb"

    # Company Page Variables
    company_logo_xpath = "//div[@class='h-logo']//a[@title='Teknasyon']"
    career_link_xpath = "//li[@id='menu-item-128']//a"

    # Career Page Variables
    description_xpath = "//div[@class='b-desc']//p"
    jobs_xpath = "//a[@class='jlb-link']"
    apply_btn_xpath = "//a[@class='button button-blue']"

    # Job Page Variables
    job_title_xpath = "//div[@class='tb-text']//h1"
    apply_title_xpath = "//div[@class='title text-center']//h1"
    error_surname_id = "jobNameSurname-error"
    error_email_id = "jobEmail-error"
    error_file_id = "jobFile-error"
    error_let_id = "jobLet-error"
    error_captcha_id = "recaptchaControl-error"
    submit_btn_xpath = "//button[@class='button button-blue']"
    surname_id = "jobNameSurname"
    email_id = "jobEmail"
    surname = "Engin"
    email = "engnsacan@gmail.com"
    captcha_box_xpath = "//div[@class='recaptcha-checkbox-border']"
    captcha_box_checkmark_xpath = "//div[@class ='recaptcha-checkbox-checkmark']"
    file_upload_id= "jobFile"
    check_boxes_xpath = "//span[@class='ci-effect']"
    captcha_iframe_xpath = "//iframe[@title='reCAPTCHA']"
    successful_message_xpath = "//div[@class='title text-center mb-0 aos-init aos-animate']/h2"
