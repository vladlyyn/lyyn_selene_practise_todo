from selene import browser, have, be, command
from selenium.webdriver.common.by import By


def test_complete_todo():
    browser.open('/')
    # browser.config.timeout = 10
    # browser.element('[class=form-control]').should(be.blank)
    browser.driver.find_element(By.CSS_SELECTOR, '[class=form-control]')

   # browser.element('[class="bi bi-dash-circle"]').click()
    browser.element('[class="bi bi-dash-circle"]').perform(command.js.click)
    browser.element('[class=form-control]').type("a!").press_enter()
    browser.element('[class=form-control]').perform(command.select_all)

    browser.element('[class=form-control]').type("b!").press_enter()
    browser.element('[class=form-control]').type("c!").press_enter()

    # использование with_ для локального изменения таймаута
    # browser.all('#odo-list>li').with_(timeout=browser.config.timeout*1.5).should(have.size(3))

    browser.all('#todo-list>li').should(have.size(3))
    browser.all('#todo-list>li').first.should(have.exact_text('a!'))
    browser.all('#todo-list>li').second.should(have.exact_text('b!'))
    browser.all('#todo-list>li')[2].should(have.exact_text('c!'))
    browser.all('#todo-list>li')[-1].should(have.exact_text('c!'))

    # всё можно записать в одну строку
    browser.all('#todo-list>li').should(have.exact_texts('a!', 'b!', 'c!'))
    # browser.all('#odo-list>li').second.element('[type="checkbox"]').click()

    (browser.all('#todo-list>li').element_by(have.exact_text('b!')).element('[type="checkbox"]').click())
    # browser.all('#odo-list>li').by(have.css_class('"form-check-label col-10"')).should(have.exact_text('b!'))

    completed = browser.all('//li[.//s]')
    completed.should(have.size(1))
    completed.first.should(have.text('b!'))

#browser.all('#odo-list>li').by(have.css_class(‘completed’))
# css класс должен содержать определенный текст:
#browser.all('#odo-list>li').element_by(have.css_class(‘completed’)).should(have.exact_texts('b!'))
#browser.all('#odo-list>li').by(have.css_class(‘completed’)).should(have.exact_texts('b!'))
#browser.all('#odo-list>li').by(have.no.css_class(‘completed’)).should(have.exact_texts('a!', 'c!'))

# xpass для клика на чекбокс
#browser.element('//li[.//s]').click()

def test_title_placing():
    browser.open('/')
    if browser.wait_until(have.title('To do - простой список дел онлайн')):
        print('NICE!')
    else:
        print('SO BAD :(')








