'''
Created on 1 Aug 2015

@author: Anna
'''

from dream.plugins import plugin

class PostProcessingOfferPhase(plugin.OutputPreparationPlugin):
  """ Output the result of offer phase in a format compatible with
  Output_viewDownloadFile
  """

  def postprocess(self, data):
    # XXX the event generator should store its result in data and not in global
    # variable.
    from dream.simulation.applications.FrozenSimulation.Globals import G
    data['result']['result_list'][-1][self.configuration_dict['output_id']] = {
      'name': 'Result.xlsx',
      'mime_type': 'application/vnd.ms-excel',
      'data': G.tabSchedule.xlsx.encode('base64')
    }
    return data