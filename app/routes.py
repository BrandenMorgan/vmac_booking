from datetime import datetime
from flask import render_template, flash, redirect, url_for, request
from werkzeug.urls import url_parse
from app import app, db
from flask_login import current_user, login_user, logout_user, login_required
from app.forms import LoginForm, RegistrationForm, EventForm, EventDetailsForm
from app.models import User, Event

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
@login_required
def index():
    form = EventForm()
    print(form.errors)

    if form.is_submitted():
        print('form submitted')

    if form.validate():
        print('valid')

    print(form.errors)

    if form.validate_on_submit():
        event = Event(event_name=form.event_name.data, promoter_name=form.promoter_name.data,
                    event_date=form.event_date.data, event_type=form.event_type.data,
                    event_manager=form.event_manager.data, deposit_amount=form.deposit_amount.data,
                    guest_count=form.guest_count.data, bar_min=form.bar_min.data,
                    other_notes=form.other_notes.data, booked=form.booked.data,
                    tsl_approved=form.tsl_approved.data, balance_paid=form.balance_paid.data,
                    contract_sent=form.contract_sent.data, cleaning=form.cleaning.data,
                    deposit_paid=form.deposit_paid.data, bar=form.bar.data)

        db.session.add(event)
        db.session.commit()
        flash('Your event has been added!')
        return redirect(url_for('index'))
    return render_template('index.html', title='Home', form=form, events=events)

@app.route('/calendar')
def calendar():
    return "This is the calendar view"

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('/login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)
    return render_template('login.html', title='Sign In', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route('/events', methods=['GET'])
def events():
    form = EventForm()
    return render_template('events.html', form=form, events = Event.query.all())
    # events.get sqlalchemy syntax

@app.route('/delete_event', methods=['GET', 'POST'])
@login_required
def delete_event():
    args = request.args
    print(args)

    id = args['id']
    print(id)

    form = EventDetailsForm()
    if form.validate_on_submit():
        print('second')
        event_data = Event.query.get(id)
        event_data.event_name = form.event_name.data
        event_data.promoter_name = form.promoter_name.data
        event_data.event_date = form.event_date.data
        event_data.event_type = form.event_type.data
        event_data.event_manager = form.event_manager.data
        event_data.deposit_amount = form.deposit_amount.data
        event_data.guest_count = form.guest_count.data
        event_data.bar_min = form.bar_min.data
        event_data.other_notes = form.other_notes.data
        event_data.booked = form.booked.data
        event_data.tsl_approved = form.tsl_approved.data
        event_data.balance_paid = form.balance_paid.data
        event_data.contract_sent = form.contract_sent.data
        event_data.cleaning = form.cleaning.data
        event_data.deposit_paid = form.deposit_paid.data
        event_data.bar = form.bar.data
        db.session.delete(event_data)
        db.session.commit()
        flash('Your event has been deleted.')
        return redirect(url_for('events'))

    elif request.method == 'GET':
        print('first')
        event_data = Event.query.get(id)
        form.event_name.data = event_data.event_name
        form.promoter_name.data = event_data.promoter_name
        form.event_date.data = event_data.event_date
        form.event_type.data = event_data.event_type
        form.event_manager.data = event_data.event_manager
        form.deposit_amount.data = event_data.deposit_amount
        form.guest_count.data = event_data.guest_count
        form.bar_min.data = event_data.bar_min
        form.other_notes.data = event_data.other_notes
        form.booked.data = event_data.booked
        form.tsl_approved.data = event_data.tsl_approved
        form.balance_paid.data = event_data.balance_paid
        form.contract_sent.data = event_data.contract_sent
        form.cleaning.data = event_data.cleaning
        form.deposit_paid.data = event_data.deposit_paid
        form.bar.data = event_data.bar

    return render_template('delete_event.html', title='Delete event',
                           form=form)




@app.route('/event_details', methods=['GET', 'POST'])
@login_required
def event_details():
    args = request.args
    print(args)

    id = args['id']
    print(id)



    form = EventDetailsForm()
    print("errors: ")
    print(form.errors)

    # if form.is_submitted():
    #     print('form submitted')
    #
    # if form.validate():
    #     print('valid')
    #
    # print(form.errors)
    if form.validate_on_submit():
        print('second')
        event_data = Event.query.get(id)
        event_data.event_name = form.event_name.data
        event_data.promoter_name = form.promoter_name.data
        event_data.event_date = form.event_date.data
        event_data.event_type = form.event_type.data
        event_data.event_manager = form.event_manager.data
        event_data.deposit_amount = form.deposit_amount.data
        event_data.guest_count = form.guest_count.data
        event_data.bar_min = form.bar_min.data
        event_data.other_notes = form.other_notes.data
        event_data.booked = form.booked.data
        event_data.tsl_approved = form.tsl_approved.data
        event_data.balance_paid = form.balance_paid.data
        event_data.contract_sent = form.contract_sent.data
        event_data.cleaning = form.cleaning.data
        event_data.deposit_paid = form.deposit_paid.data
        event_data.bar = form.bar.data
        db.session.commit()
        flash('Your changes have been saved.')
        return redirect(url_for('events'))

    elif request.method == 'GET':
        print('first')
        event_data = Event.query.get(id)
        form.event_name.data = event_data.event_name
        form.promoter_name.data = event_data.promoter_name
        form.event_date.data = event_data.event_date
        form.event_type.data = event_data.event_type
        form.event_manager.data = event_data.event_manager
        form.deposit_amount.data = event_data.deposit_amount
        form.guest_count.data = event_data.guest_count
        form.bar_min.data = event_data.bar_min
        form.other_notes.data = event_data.other_notes
        form.booked.data = event_data.booked
        form.tsl_approved.data = event_data.tsl_approved
        form.balance_paid.data = event_data.balance_paid
        form.contract_sent.data = event_data.contract_sent
        form.cleaning.data = event_data.cleaning
        form.deposit_paid.data = event_data.deposit_paid
        form.bar.data = event_data.bar
        form.id.data = event_data.id

    return render_template('event_details.html', title='Event Details',
                           form=form)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)
