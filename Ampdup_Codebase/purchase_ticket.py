from flask import Blueprint, request, render_template, redirect, url_for, session, flash, make_response
from flask_login import login_required


purchase_ticket_bp = Blueprint('PurchaseTicket', __name__)


@purchase_ticket_bp.route('/Purchase_Ticket', methods=['POST'])

def purchase_ticket(event_id):
    
    if 'user_name' not in session:
        flash('Please log in to purchase tickets')
        return redirect(url_for('auth.login'))
    
    ga_Ticket = int(request.form.get('GA_Ticket', 0))
    
    if ga_Ticket == '0':
        flash('Please select at least one ticket to purchase.')
        return redirect(url_for('main.EventDetails'))
    
    session['booking']= ga_Ticket

    flash('Purchase successful!')
    return redirect(url_for('main.BookingHistory'))    
    
