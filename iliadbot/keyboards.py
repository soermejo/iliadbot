# iliadbot - A telegram bot to check your iliad's balance and quotas
# Copyright (C) 2018  iliadbot authors: see AUTHORS file at the top-level directory of this repo
#
# iliadbot is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published
# by the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# iliadbot is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with iliadbot.  If not, see <http://www.gnu.org/licenses/>.


import collections
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from iliadbot import emoji


def update_iliad_data_kb(iliad_id, iliad_password, info):
    buttons = collections.OrderedDict()
    buttons['italia'] = '{} Soglie Italia'.format(emoji.italy)
    buttons['estero'] = '{} Soglie Estero'.format(emoji.earth)
    buttons['info_sim'] = '{} Info Sim'.format(emoji.info)

    buttons_list = []
    for i in buttons:

        if i == info:
            pre_current_choice = "{} ".format(emoji.current_choice)
            update_text =  "(Aggiorna {})".format(emoji.re_load)
            post_current_choice = " {}".format(emoji.current_choice)
        else:
            pre_current_choice = ""
            update_text =  ""
            post_current_choice = "" 

        buttons_list.append([
            InlineKeyboardButton(
                text="{pre_current_choice}{button_text} {aggiorna}{post_current_choice}".format(
                    pre_current_choice=pre_current_choice,
                    button_text=buttons[i], 
                    aggiorna=update_text,
                    post_current_choice=post_current_choice
                ),
                callback_data="update_iliad:{}:{}:{}".format(iliad_id, iliad_password, i)
            )
        ])
    keyboard = InlineKeyboardMarkup(buttons_list)
    return keyboard
