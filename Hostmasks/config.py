###
# Copyright (c) 2013, GLolol (GLolol1@hotmail.com)
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
# * Redistributions of source code must retain the above copyright notice, this
# list of conditions and the following disclaimer.
#
# * Redistributions in binary form must reproduce the above copyright notice,
# this list of conditions and the following disclaimer in the documentation
# and/or other materials provided with the distribution.
#
# * Neither the name of the software nor the names of its
# contributors may be used to endorse or promote products derived from
# this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
# FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
# DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
# SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
# OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
###

import supybot.conf as conf
import supybot.registry as registry
try:
    from supybot.i18n import PluginInternationalization
    _ = PluginInternationalization('Hostmasks')
except:
    # Placeholder that allows to run the plugin on a bot
    # without the i18n module
    _ = lambda x:x

def configure(advanced):
    # This will be called by supybot to configure this module.  advanced is
    # a bool that specifies whether the user identified himself as an advanced
    # user or not.  You should effect your configuration by manipulating the
    # registry as appropriate.
    from supybot.questions import expect, anything, something, yn
    conf.registerPlugin('Hostmasks', True)

Hostmasks = conf.registerPlugin('Hostmasks')

class BantypeValue(registry.OnlySomeStrings):
    validStrings = ('1', '2', '3', '4')
conf.registerGlobalValue(Hostmasks, 'banType',
    BantypeValue('4', _("""Chooses the preferred ban type for the
        banmask command. 1 = *!*@address.isp.net; 2 = *!~ident@address.isp.net;
         3 = *!*@*.isp.net; 4 = *!~ident@*.isp.net""")))
         
conf.registerGlobalValue(Hostmasks, 'smartBans',
    registry.Boolean(False, _("""Allow the bot to attempt to detect vHosts and other
         host cloaks, adjusting its banmask output depending on the hostmask
         it finds. This overrides the banType setting if such vHost is detected.""")))

# This is where your configuration variables (if any) should go.  For example:
# conf.registerGlobalValue(Hostmasks, 'someConfigVariableName',
#     registry.Boolean(False, _("""Help for someConfigVariableName.""")))


# vim:set shiftwidth=4 tabstop=4 expandtab textwidth=79: